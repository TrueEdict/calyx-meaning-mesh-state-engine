from dataclasses import dataclass
from enum import Enum


class InformationRoute(str, Enum):
    INTERNAL = "internal"
    EXTERNAL = "external"
    MIXED = "mixed"


class ExecutionRoute(str, Enum):
    DIRECT = "route_0_direct"
    DEEPSEEK = "route_1_deepseek"
    PLAN_THEN_CODE = "route_2_glm_plan_deepseek_code"
    GLM_DIRECT = "route_3_glm_direct"


@dataclass(frozen=True)
class IssueSignals:
    project_memory_coverage: float = 0.0
    local_reproduction_strength: float = 0.0
    prior_issue_match: float = 0.0
    missing_external_fact: float = 0.0
    external_dependency_signal: float = 0.0
    scope: float = 0.0
    dependency_depth: float = 0.0
    ambiguity: float = 0.0
    novelty: float = 0.0
    blocker_recurrence: float = 0.0
    verification_fragility: float = 0.0
    production_risk: float = 0.0
    causal_uncertainty: float = 0.0
    plan_separability: float = 1.0
    code_required: bool = True


@dataclass(frozen=True)
class RouteDecision:
    information_route: InformationRoute
    execution_route: ExecutionRoute
    complexity: float
    plan_separability: float
    planner_model: str | None
    coder_model: str | None
    provider: str
    reasons: tuple[str, ...]
